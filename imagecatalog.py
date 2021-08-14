"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 08/04/2021
Term Project
The Image Catalog class
"""
import csv
import logging
from pathlib import Path

import appglobals
from image import Image
import imageattributes
from imagerating import ImageRating

logger = logging.getLogger(__name__)

# dictionary key constants
K_NAME = 'name'
K_RATING = 'rating'
K_IMG = 'img'
K_PATH = 'path'


class ImageCatalog:
    """
    The image catalog
    """
    IMAGE_FILESPEC = '*.jpg'

    def __init__(self, directory: str):
        """
        Constructor
        """
        self.image_path = Path(directory)
        self.image_files = \
            list(self.image_path.glob(ImageCatalog.IMAGE_FILESPEC))
        self.__image_records = ImageCatalog.__build_images(self.image_files)
        logger.info('catalog has loaded {} files.', len(self.image_files))
        self.__ratings_path = \
            self.image_path / appglobals.app_config_ratings_filename
        self.load_ratings()

    @staticmethod
    def __build_images(image_files_list: list):
        """
        create a list of records of images from the list of path

        :param image_files_list: image paths
        :return: record list
        """
        # todo maybe optimize by lazy loading the 'img' property
        return [{K_PATH: p, K_IMG: Image(p)} for p in image_files_list]

    def __len__(self):
        """
        Returns the number of images in the catalog
        :return:
        """
        return len(self.__image_records)

    def __getitem__(self, item) -> dict:
        """
        return the image at specified index
        :return:
        """
        return self.__image_records[item]

    def __repr__(self):
        """
        str()
        :return:
        """
        return 'ImageCatalog [{}] has {} images'.format(self.image_path,
                                                        len(self.image_files))

    def get_ratings_path(self):
        """
        Ratings path

        :return:
        """
        return self.__ratings_path

    def load_ratings(self):
        """
        load the ratings
        :return:
        """
        logger.info('loading ratings file from {}'
                    .format(self.__ratings_path))

        ratings = []
        try:
            with open(self.__ratings_path) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    ratings.append(row)
        except IOError as err:
            logger.error(f'Unable to load ratings due to error {err}')
            return False
        else:
            self.__apply_ratings(ratings)
            return True

    def __apply_ratings(self, ratings):
        """
        Internal method to apply the ratings to the images from the catalog
        from the ratings file
        :param ratings: ratings list
        :return: None
        """
        for rec in self.__image_records:
            name = rec[K_IMG].get_name()
            rating = ImageCatalog.__find_rating(name, ratings)
            rec[K_IMG].set_rating(ImageRating(rating))

    @staticmethod
    def __find_rating(name, ratings):
        """
        find the rating in list with specified name; note that not all entries
        in the directory will automatically have an entry in the ratings file
        so we need to 'find' it; if not found return 0 (no rating)

        :param name: name of image
        :param ratings: list
        :return: ImageRating object
        """
        first_or_default = next(filter(lambda r: r[K_NAME] == name, ratings),
                                None)
        try:
            return ImageRating.MIN_RATING if first_or_default is None \
                else int(first_or_default[K_RATING])
        except ValueError as err:
            logger.error(
                'Invalid rating for {} found; returning {} instead'
                .format(name,
                        ImageRating.MIN_RATING))
            return 0

    def save_ratings(self):
        """
        save the ratings
        :return:
        """
        # we are only going to save the ratings which are non-zero
        non_zero_ratings = list(
            map(lambda mrec: {K_NAME: mrec[K_IMG].get_name(),
                              K_RATING: int(mrec[K_IMG].get_rating())},
                filter(lambda frec: int(frec[K_IMG].get_rating()) != 0,
                       self.__image_records)))

        logger.info('writing {} ratings to {}'
                    .format(len(non_zero_ratings),
                            self.__ratings_path))

        try:
            with open(self.__ratings_path, 'w') as csv_file:
                csv_writer = csv.DictWriter(csv_file,
                                            fieldnames=[K_NAME, K_RATING])
                csv_writer.writeheader()
                for rec in non_zero_ratings:
                    csv_writer.writerow(rec)
        except IOError as err:
            logger.error(f'Unable to write ratings due to error {err}')
            return False
        else:
            return True

    def set_rating(self, index: int, rating: int):
        """
        set rating at specified index

        :param index: the index
        :param rating: rating
        :return: the updated image with the rating
        """
        return self.__image_records[index][K_IMG].set_rating(
            ImageRating(rating))

    def get_stats(self):
        """
        the statistics

        :return:
        """
        unique_camera_brands = set(rec[K_IMG].get_attributes()
                                   .attr_dict.get(imageattributes.EXIF_MAKE,
                                                  None)
                                   for rec in self.__image_records)

        # remove None in the list
        unique_camera_brands.remove(None)
        stats = {'Total Images': len(self.__image_records),
                 'Camera Brands': unique_camera_brands}

        return stats
