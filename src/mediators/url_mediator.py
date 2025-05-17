from __future__ import annotations
from dataclasses import dataclass

from ..crawlers.leetcode_crawler import LeetcodeCrawler
from ..helpers.model.finders.provider_finder import ProviderFinder
from ..models.contest import Contest
from ..helpers.config.local_config import LocalConfig
from ..helpers.terminal.arg_helper import ArgHelper


@dataclass
class URLMediator:
    url: str
    contest: Contest

    @staticmethod
    def instance() -> URLMediator:
        url = (
            ArgHelper(attributes=["url"], prefix="--")
            .check_help()
            .must_include("url")
            .get_data()
        )["url"]
        contest_data = (
            ArgHelper(
                attributes=Contest.modifiables(),
                data=LocalConfig.read("contest"),
                prefix="--",
            )
            .check_help()
            .check_args(skipps=["url"])
            .get_data()
        )
        return URLMediator(url, Contest.from_dict(contest_data))

    def extract_info(self) -> URLMediator:
        if "leetcode.com" in self.url:
            self.contest.provider = ProviderFinder.by_abbreviation("lc")
        return self

    def extract_snippet(self) -> URLMediator:
        crawler = LeetcodeCrawler(url=self.url)  # TODO: Crawler Abastract.
        self.snippet = crawler.get_snippet()
        self.tests = crawler.get_tests()
        return self

    def extract_tests(self) -> URLMediator:
        return self

    def generate(self) -> URLMediator:
        return self

    def closure(self) -> URLMediator:
        print("Done!")
        return self
