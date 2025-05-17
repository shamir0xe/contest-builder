from dataclasses import dataclass, field
from typing import List, Tuple
import re
from pylib_0xe.buffer_io.buffer_reader import BufferReader
from pylib_0xe.buffer_io.string_buffer import StringBuffer


def problem_name_mapper(name: str) -> str:
    name = name.lower()
    name = re.sub(r"(\(|\)|\[|\])", "", name)
    name = re.sub(r"(\.|\\|\/|\,|\:|\;|\'|\")", " ", name)
    name = re.sub(r"\s+", "-", name.strip())
    name = re.sub(r"\-+", "-", name)
    name = re.sub(r"div\-(\d+)", r"div\1", name)
    name = re.sub(r"\-(\+|\>|\<)\-", r"\1", name)
    return name


@dataclass
class LeetcodeCrawler:
    url: str

    def __post_init__(self) -> None:
        self.data = ""

    def get_snippet(self) -> str:
        return ""

    def get_tests(self) -> List[Tuple[str, str]]:
        return []


user_contests = "query ($username: String!) {\n    userContestRanking(username: $username) {\n        attendedContestsCount\n        rating\n        globalRanking\n        totalParticipants\n        topPercentage\n        badge {\n            name\n        }\n    }\n    userContestRankingHistory(username: $username) {\n        attended\n        trendDirection\n        problemsSolved\n        totalProblems\n        finishTimeInSeconds\n        rating\n        ranking\n        contest {\n            title\n            startTime\n        }\n    }\n}\n"

# // src/graphql/daily.graphql?raw
daily_default = "query {\n    activeDailyCodingChallengeQuestion {\n        date\n        link\n        question {\n            questionId\n            questionFrontendId\n            boundTopicId\n            title\n            titleSlug\n            content\n            translatedTitle\n            translatedContent\n            isPaidOnly\n            difficulty\n            likes\n            dislikes\n            isLiked\n            similarQuestions\n            exampleTestcases\n            contributors {\n                username\n                profileUrl\n                avatarUrl\n            }\n            topicTags {\n                name\n                slug\n                translatedName\n            }\n            companyTagStats\n            codeSnippets {\n                lang\n                langSlug\n                code\n            }\n            stats\n            hints\n            solution {\n                id\n                canSeeDetail\n                paidOnly\n                hasVideoSolution\n                paidOnlyVideo\n            }\n            status\n            sampleTestCase\n            metaData\n            judgerAvailable\n            judgeType\n            mysqlSchemas\n            enableRunCode\n            enableTestMode\n            enableDebugger\n            envInfo\n            libraryUrl\n            adminUrl\n            challengeQuestion {\n                id\n                date\n                incompleteChallengeCount\n                streakCount\n                type\n            }\n            note\n        }\n    }\n}\n"

# // src/graphql/leetcode-cn/user-progress-questions.graphql?raw
user_progress_questions_default = 'query userProgressQuestionList($filters: UserProgressQuestionListInput) {\n    userProgressQuestionList(filters: $filters) {\n        totalNum\n        questions {\n            translatedTitle\n            frontendId\n            title\n            titleSlug\n            difficulty\n            lastSubmittedAt\n            numSubmitted\n            questionStatus\n            lastResult\n            topicTags {\n                name\n                nameTranslated\n                slug\n            }\n        }\n    }\n}\n\n# UserProgressQuestionListInput:\n# {\n#     "filters": {\n#         "skip": 10,\n#         "limit": 10,\n#         "questionStatus": "SOLVED", // Enums: SOLVED, ATTEMPTED\n#         "difficulty": [\n#             "EASY",\n#             "MEDIUM",\n#             "HARD"\n#         ]\n#     }\n# }\n'

# // src/graphql/problem.graphql?raw
problem_default = "query ($titleSlug: String!) {\n    question(titleSlug: $titleSlug) {\n        questionId\n        questionFrontendId\n        boundTopicId\n        title\n        titleSlug\n        content\n        translatedTitle\n        translatedContent\n        isPaidOnly\n        difficulty\n        likes\n        dislikes\n        isLiked\n        similarQuestions\n        exampleTestcases\n        contributors {\n            username\n            profileUrl\n            avatarUrl\n        }\n        topicTags {\n            name\n            slug\n            translatedName\n        }\n        companyTagStats\n        codeSnippets {\n            lang\n            langSlug\n            code\n        }\n        stats\n        hints\n        solution {\n            id\n            canSeeDetail\n            paidOnly\n            hasVideoSolution\n            paidOnlyVideo\n        }\n        status\n        sampleTestCase\n        metaData\n        judgerAvailable\n        judgeType\n        mysqlSchemas\n        enableRunCode\n        enableTestMode\n        enableDebugger\n        envInfo\n        libraryUrl\n        adminUrl\n        challengeQuestion {\n            id\n            date\n            incompleteChallengeCount\n            streakCount\n            type\n        }\n        note\n    }\n}\n"

# // src/graphql/problems.graphql?raw
problems_default = "query ($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n    problemsetQuestionList: questionList(\n        categorySlug: $categorySlug\n        limit: $limit\n        skip: $skip\n        filters: $filters\n    ) {\n        total: totalNum\n        questions: data {\n            acRate\n            difficulty\n            freqBar\n            questionFrontendId\n            isFavor\n            isPaidOnly\n            status\n            title\n            titleSlug\n            topicTags {\n                name\n                id\n                slug\n            }\n            hasSolution\n            hasVideoSolution\n        }\n    }\n}\n"

# // src/graphql/profile.graphql?raw
profile_default = "query ($username: String!) {\n    allQuestionsCount {\n        difficulty\n        count\n    }\n    matchedUser(username: $username) {\n        username\n        socialAccounts\n        githubUrl\n        contributions {\n            points\n            questionCount\n            testcaseCount\n        }\n        profile {\n            realName\n            websites\n            countryName\n            skillTags\n            company\n            school\n            starRating\n            aboutMe\n            userAvatar\n            reputation\n            ranking\n        }\n        submissionCalendar\n        submitStats {\n            acSubmissionNum {\n                difficulty\n                count\n                submissions\n            }\n            totalSubmissionNum {\n                difficulty\n                count\n                submissions\n            }\n        }\n        badges {\n            id\n            displayName\n            icon\n            creationDate\n        }\n        upcomingBadges {\n            name\n            icon\n        }\n        activeBadge {\n            id\n        }\n    }\n    recentSubmissionList(username: $username, limit: 20) {\n        title\n        titleSlug\n        timestamp\n        statusDisplay\n        lang\n    }\n}\n"

# // src/graphql/recent-submissions.graphql?raw
recent_submissions_default = "query ($username: String!, $limit: Int) {\n    recentSubmissionList(username: $username, limit: $limit) {\n        title\n        titleSlug\n        timestamp\n        statusDisplay\n        lang\n    }\n}\n"

# // src/graphql/submission-detail.graphql?raw
submission_detail_default = "query submissionDetails($id: Int!) {\n    submissionDetails(submissionId: $id) {\n        id\n        runtime\n        runtimeDisplay\n        runtimePercentile\n        runtimeDistribution\n        memory\n        memoryDisplay\n        memoryPercentile\n        memoryDistribution\n        code\n        timestamp\n        statusCode\n        user {\n            username\n            profile {\n                realName\n                userAvatar\n            }\n        }\n        lang {\n            name\n            verboseName\n        }\n        question {\n            questionId\n            titleSlug\n            hasFrontendPreview\n        }\n        notes\n        flagType\n        topicTags {\n            tagId\n            slug\n            name\n        }\n        runtimeError\n        compileError\n        lastTestcase\n        codeOutput\n        expectedOutput\n        totalCorrect\n        totalTestcases\n        fullCodeOutput\n        testDescriptions\n        testBodies\n        testInfo\n        stdOutput\n    }\n}\n"

# // src/graphql/submissions.graphql?raw
submissions_default = "query ($offset: Int!, $limit: Int!, $slug: String) {\n    submissionList(offset: $offset, limit: $limit, questionSlug: $slug) {\n        hasNext\n        submissions {\n            id\n            lang\n            time\n            timestamp\n            statusDisplay\n            runtime\n            url\n            isPending\n            title\n            memory\n            titleSlug\n        }\n    }\n}\n"

# // src/graphql/whoami.graphql?raw
whoami_default = "query {\n    userStatus {\n        userId\n        username\n        avatar\n        isSignedIn\n        isMockUser\n        isPremium\n        isAdmin\n        isSuperuser\n        isTranslator\n        permissions\n    }\n}\n"

contest_default = """
query panelQuestionList($currentQuestionSlug: String!, $categorySlug: String, $envId: String, $envType: String, $filters: QuestionListFilterInput) {
  panelQuestionList(
    currentQuestionSlug: $currentQuestionSlug
    categorySlug: $categorySlug
    envId: $envId
    envType: $envType
    filters: $filters
  ) {
    hasViewPermission
    panelName
    finishedLength
    totalLength
    questions {
      difficulty
      id
      paidOnly
      questionFrontendId
      status
      title
      titleSlug
      score
      questionNumber
      topicTags {
        name
        slug
      }
    }
  }
}
"""


import asyncio
import json
import time
from datetime import datetime
from typing import Any, Dict, List, Optional
from aiohttp import ClientSession

# Constants
BASE_URL = "https://leetcode.com"
BASE_URL_CN = "https://leetcode.cn"
USER_AGENT = "Mozilla/5.0 LeetCode API"


# Cache Implementation
class Cache:
    def __init__(self):
        self._table = {}

    def get(self, key: str) -> Any:
        item = self._table.get(key)
        if item:
            if item["expires"] > time.time() * 1000:
                return item["value"]
            self.remove(key)
        return None

    def set(self, key: str, value: Any, expires: int = 60000) -> None:
        self._table[key] = {
            "key": key,
            "value": value,
            "expires": (time.time() * 1000 + expires) if expires > 0 else 0,
        }

    def remove(self, key: str) -> None:
        self._table.pop(key, None)

    def clear(self) -> None:
        self._table = {}

    def load(self, json_str: str) -> None:
        self._table = json.loads(json_str)


cache = Cache()
caches = {"default": cache}


# Utility Functions
def parse_cookie(cookie: str) -> Dict[str, str]:
    return {
        k.strip().split("=")[0]: v.strip()
        for part in cookie.split(";")
        if "=" in part
        for k, v in [part.split("=", 1)]
    }


# Credential Management
class Credential:
    def __init__(self, data: Optional[Dict[str, Any]] = None):
        self.session = None
        self.csrf = None
        if data:
            self.session = data.get("session")
            self.csrf = data.get("csrf")

    async def init(self, session: str = "") -> "Credential":
        self.csrf = await self.get_csrf()
        if session:
            self.session = session
        return self

    @staticmethod
    async def get_csrf() -> Optional[str]:
        async with ClientSession() as session:
            async with session.get(
                f"{BASE_URL}/graphql/", headers={"User-Agent": USER_AGENT}
            ) as response:
                cookies = parse_cookie(response.headers.get("Set-Cookie", ""))
                return cookies.get("csrftoken")


# Rate Limiting and Concurrency Control
class Mutex:
    def __init__(self, space: int = 1):
        self.space = space
        self.used = 0
        self._lock = asyncio.Lock()
        self._waiters = []

    async def lock(self) -> int:
        async with self._lock:
            if self.used >= self.space:
                future = asyncio.Future()
                self._waiters.append(future)
                await future
            self.used += 1
            return self.used

    async def unlock(self) -> int:
        async with self._lock:
            if self.used <= 0:
                return 0
            self.used -= 1
            if self._waiters:
                future = self._waiters.pop(0)
                future.set_result(None)
            return self.used


class RateLimiter(Mutex):
    def __init__(self, limit: int = 20, interval: int = 10000, concurrent: int = 2):
        super().__init__(concurrent)
        self.count = 0
        self.last = 0
        self.interval = interval
        self.time_mutex = Mutex(limit)
        self.timer = None

    async def lock(self) -> int:
        if self.last + self.interval < time.time() * 1000:
            await self.reset()
        await self.time_mutex.lock()
        self.count += 1
        return await super().lock()

    async def reset(self) -> None:
        while self.count > 0:
            await self.time_mutex.unlock()
            self.count -= 1
        self.last = time.time() * 1000


# Core LeetCode Client
class LeetCode:
    def __init__(self, credential: Optional[Credential] = None, cache: Cache = cache):
        self.credential = credential or Credential()
        self.cache = cache
        self.limiter = RateLimiter()
        self.initialized = asyncio.Event()
        self._init_task = asyncio.create_task(self._initialize())

    async def _initialize(self):
        if not self.credential.csrf:
            await self.credential.init()
        self.initialized.set()

    async def graphql(self, query: Dict[str, Any]) -> Dict[str, Any]:
        await self.initialized.wait()
        # async with self.limiter.lock():
        # TODO: impl lock correctly
        async with ClientSession() as session:
            headers = {
                "Content-Type": "application/json",
                "User-Agent": USER_AGENT,
                "X-CSRFToken": self.credential.csrf or "",
                "Cookie": f"csrftoken={self.credential.csrf}; LEETCODE_SESSION={self.credential.session}",
            }
            async with session.post(
                f"{BASE_URL}/graphql", headers=headers, json=query
            ) as response:
                response.raise_for_status()
                if response.headers.get("Set-Cookie"):
                    cookies = parse_cookie(response.headers["Set-Cookie"])
                    if "csrftoken" in cookies:
                        self.credential.csrf = cookies["csrftoken"]
                return await response.json()

    # Example API Methods
    async def user(self, username: str) -> Dict[str, Any]:
        query = {
            "variables": {"username": username},
            "query": profile_default,  # Should define GraphQL constants
        }
        response = await self.graphql(query)
        return response["data"]

    async def daily(self) -> Dict[str, Any]:
        response = await self.graphql({"query": daily_default})
        return response["data"]["activeDailyCodingChallengeQuestion"]

    async def problem(self, name: str) -> Dict[str, Any]:
        name = problem_name_mapper(name)
        print(f"Going to fetch '{name}'")
        response = await self.graphql(
            {"query": problem_default, "variables": {"titleSlug": name}}
        )
        data = response["data"]["question"]
        snippet = ""

        for entry in data["codeSnippets"]:
            if "langSlug" in entry and entry["langSlug"] == "cpp":
                # get the cpp snippet
                snippet = entry["code"]

        tests = data["exampleTestcases"].encode().decode("unicode_escape")
        metadata = json.loads(data["metaData"])

        print(tests)
        print(metadata)
        return {"snippet": snippet, "tests": tests, "metadata": metadata}

    async def contest(self, name: str) -> Dict[str, Any]:
        res = {}
        name = problem_name_mapper(name)
        print(f"Going to fetch contest {name}")
        response = await self.graphql(
            {
                "query": contest_default,
                "variables": {
                    "currentQuestionSlug": "properties-graph",
                    "envId": name,
                    "envType": "contest",
                },
            }
        )
        data = response["data"]
        print(json.dumps(data, indent=2))
        return data


template = """
#include <bits/stdc++.h>

/**
 * problem {:problem_alphabet} ({:problem_number}/{:total_problems})
 * {:provider}, {:contest_name}
 * author: @{:author}
 * generated by contest-builder
 * https://github.com/shamir0xe/contest-builder
 **/

typedef long long ll;
typedef std::pair<int, int> pii;
typedef std::vector<int> vi;
typedef std::vector<long long> vl;
typedef std::vector<std::vector<int>> vvi;
typedef std::vector<std::vector<ll>> vvl;
#define range(i, n) for (int i = 0; i < n; ++i)
#define rrange(i, n) for (int i = n - 1; i >= 0; --i)
#define fr(i, a, n) for (int i = a; i < n; ++i)
#define rfr(i, a, n) for (int i = n - 1; i >= a; --i)
#define trace(x) std::cerr << #x << " : " << x << std::endl
#define _ << " " <<
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#define X first
#define Y second

/**
 * printing tuples
 **/
template <size_t n, typename... T>
typename std::enable_if<(n >= sizeof...(T))>::type
__tuple_printer(std::ostream &os, const std::tuple<T...> &tup) {};

template <size_t n, typename... T>
typename std::enable_if<(n < sizeof...(T))>::type
__tuple_printer(std::ostream &os, const std::tuple<T...> &tup) {
    if (n != 0) {
        os << " ";
    }
    os << std::get<n>(tup);
    __tuple_printer<n + 1>(os, tup);
};

template <typename... T>
std::ostream &operator<<(std::ostream &os, const std::tuple<T...> &tup) {
    os << "(";
    __tuple_printer<0>(os, tup);
    os << ")";
    return os;
}

/**
 * printing pairs
 **/
template <typename T, typename K>
std::ostream &operator<<(std::ostream &os, const std::pair<T, K> &p) {
    os << "(" << p.first << " " << p.second << ")";
    return os;
}

/**
 * printing vectors
 **/
template <class T>
std::ostream &operator<<(std::ostream &os, const std::vector<T> &v) {
    os << "[";
    bool first = true;
    for (auto ii = v.begin(); ii != v.end(); ++ii) {
        if (first) {
            first = false;
        } else {
            os << " ";
        }
        os << (*ii);
    }
    os << "]";
    return os;
}

template <typename T, typename K = std::function<void(void)>>
void smin(T &a, T b, const K callable = []() {}) {
    if (a > b) {
        a = b;
        callable();
    }
}

template <typename T, typename K = std::function<void(void)>>
void smax(T &a, T b, const K callable = []() {}) {
    if (a < b) {
        a = b;
        callable();
    }
}

/**
 * define variables here
 **/
const int maxn = 1000 * 100 + 5;

/**
 * define functions here
 **/

//{:snippet}
//{:cutoff}
//{:tests}
//{:main}
"""


@dataclass
class TestCreator:
    test_name: str
    func_name: str
    return_type: str
    current: str = field(default="")
    params: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        return_type = self.type_mapper(self.return_type)
        self.current = f"{return_type} {self.test_name}() {{\n"

    def add_parameter(self, param_name: str, param_type: str, value: str) -> None:
        self.params += [param_name]
        mapped_type = self.type_mapper(param_type)
        mapped_value = self.value_mapper(param_type, BufferReader(StringBuffer(value)))
        print(f"-{mapped_type}- |{mapped_value}|")
        if mapped_value[0] != "{":
            mapped_value = f"{{{mapped_value}}}"
        self.current += f"    {mapped_type} {param_name}{mapped_value};\n"

    def final(self) -> str:
        self.current += f"    {self.type_mapper(self.return_type)} res = Solution().{self.func_name}("
        for i in range(len(self.params)):
            if i != 0:
                self.current += ", "
            self.current += self.params[i]
        self.current += ");\n    return res;\n}\n"
        return self.current

    def type_mapper(self, param_type: str) -> str:
        if param_type == "integer":
            return "int"
        if param_type == "string":
            return "std::string"
        if param_type == "boolean":
            return "bool"
        if param_type == "double":
            return "double"
        if param_type == "float":
            return "float"
        if param_type == "long":
            return "long long"
        if param_type[: len("list<")] == "list<":
            return f"std::vector<{self.type_mapper(param_type[len("list<") : -1])}>"
        if param_type[-2:] == "[]":
            return f"std::vector<{self.type_mapper(param_type[:-2])}>"
        raise Exception(f"Invalid Type: {param_type}")

    def next_param(self, parameter: str) -> str:
        if parameter[-2:] == "[]":
            return parameter[:-2]
        if parameter[: len("list<")] == "list<":
            return parameter[len("list<") : -1]
        return ""

    def value_mapper(self, param_type: str, reader: BufferReader) -> str:
        res = ""
        print(f"-{param_type}-  |{reader.next_char(True)}|")

        def escape_spaces():
            while not reader.end_of_buffer() and reader.is_space_char(
                reader.next_char(True)
            ):
                reader.next_char()

        if self.next_param(param_type):
            res = "{"
            while reader.next_char() != "[":
                pass
            first = True
            escape_spaces()
            while reader.next_char(True) != "]":
                if first:
                    first = False
                else:
                    res += ", "
                res += self.value_mapper(self.next_param(param_type), reader)
                print(f"~~{res} // {param_type}")
                if reader.next_char(True) == ",":
                    reader.next_char()
                    escape_spaces()
            reader.next_char()
            escape_spaces()
            res += "}"
        else:
            if param_type == "string":
                while reader.next_char(True) != '"':
                    reader.next_char()
                reader.next_char()
                res += '"'
                while reader.next_char(True) != '"':
                    temp = reader.next_char()
                    if not temp:
                        raise Exception(f"Invalid Argument {reader.next_string()}")
                    res += temp
                res += '"'
                reader.next_char()
                escape_spaces()
            else:

                def good(char: Optional[str]) -> bool:
                    if not char:
                        return False
                    if ord("0") <= ord(char) <= ord("9"):
                        return True
                    if char in [".", "+", "-"]:
                        return True
                    return False

                cur = ""
                while good(reader.next_char(True)):
                    cur += reader.next_char()  # type:ignore
                res += cur
                escape_spaces()

        return res


def main_creator(test_count: int) -> str:
    res = "int main() {\n"
    spaces = " " * 4
    for i in range(test_count):
        res += f"{spaces} auto res_{i+1} = test_{i+1}();\n"
        res += f'{spaces} std::cout << "test #{i+1}: " << res_{i+1} << std::endl;\n\n'
    res += f"{spaces} return 0;\n}}\n"
    return res


# Example usage
async def main():
    import sys

    credential = await Credential().init()
    leetcode = LeetCode(credential)
    values = await leetcode.contest("Weekly Contest 442")
    return values


    values = await leetcode.problem(" ".join(sys.argv[1:]))

    snippet = values["snippet"]
    tests = values["tests"]
    metadata = values["metadata"]

    code = snippet
    code += "\n"

    counter = 1
    try:
        params = metadata["params"]
        test_reader = BufferReader(StringBuffer(tests))
        while not test_reader.end_of_buffer():
            tc = TestCreator(
                test_name=f"test_{counter}",
                func_name=metadata["name"],
                return_type=metadata["return"]["type"],
            )
            counter += 1
            for param in params:
                tc.add_parameter(
                    param_name=param["name"],
                    param_type=param["type"],
                    value=test_reader.next_line(),
                )
            code += tc.final()
            code += "\n"
    except Exception as e:
        print(f"Error: Cannot build test cases: {str(e)}")

    code += main_creator(test_count=counter - 1)

    print(code)


if __name__ == "__main__":
    asyncio.run(main())
