from github import Github
import time
from datetime import datetime
import os

DAY_SEC = 86400
ACCESS_TOKEN = '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'
g = Github(ACCESS_TOKEN)


end_time = time.time()
start_time = end_time - DAY_SEC

# depend on time and cost
for i in range(3):
    try:
        start_time_str = datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d')
        end_time_str = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d')
        query = f'language:c++ created:{start_time_str}..{end_time_str}'
        print(query)
        end_time -= DAY_SEC
        start_time -= DAY_SEC
        result = g.search_repositories(query)
        print(result.totalCount)

        for repository in result:
            # print(f"{repository._clone_url}")
            print(f"{repository.clone_url}")
            print(f"{repository.tags_url}")
            # print(dir(repository))

            os.system(f'git clone {repository.clone_url} repos/{repository.owner.login}/{repository.name}')
            print(f"current start time {start_time}")
    except Exception as e:
        print(str(e))
        time.sleep(120)
