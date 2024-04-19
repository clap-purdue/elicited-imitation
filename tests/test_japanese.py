# -*- coding: utf-8 -*-

import unittest
from ei.japanese import JapaneseUtils


class TestJapaneseUtils(unittest.TestCase):

    j = JapaneseUtils()

    def test_mecab_tagger_owakati(self):
        text = "日本語の文章を分かち書きしたい。"
        res = self.j.mecab_tagger_owakati(text).strip()
        output = "日本 語 の 文章 を 分かち書き し たい 。"
        self.assertEqual(res, output)

    def test_clean_text(self):
        text = "日本語の文章を分かち書きし、たい。"
        res = self.j.clean_text(text)
        output = "日本語の文章を分かち書きしたい"
        self.assertEqual(res, output)


if __name__ == '__main__':
    unittest.main()



