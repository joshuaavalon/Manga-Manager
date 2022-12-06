import unittest

from src.MangaManager_ThePromidius.MetadataManager.comicinfo import AgeRating, Manga, YesNo, format_list


class LoadedCInfo_Utils(unittest.TestCase):
    def test_ComicInfo_ToList_methods_work(self):
        classes_to_test_list_implementation = (AgeRating, Manga, YesNo)

        for class_ in classes_to_test_list_implementation:
            with self.subTest("Testing {class_} has list method"):
                self.assertTrue(len(class_.list()) > 1)
        with self.subTest("Testing format_list is populated"):
            self.assertTrue(len(format_list) > 1)
