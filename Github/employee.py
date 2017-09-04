#!/usr/bin/python3
# encoding: utf-8

class EmployCommit:
    def __init__(self, name, commits_tot = 0, commits = []):
        self.name = name
        self.commits_tot = commits_tot
        self.commits = commits
    ## 当前员工总 commit 自加方法
    def add_commits_tot(self):
        self.commits_tot += 1
    ## 增加 commit 
    def add_commit(self, commit):
        self.commits.append(commit)
    ## 展示该员工 commit 记录，输出至 log
    def show_commit_tot(self):
        print("\t", self.name)
        for commit in self.commits:
            print()
            print(repr(commit['sha']).ljust(20), repr(commit['time']).ljust(30))
            print(repr(commit['url']).ljust(20))
            print()
    ## 将该员工的commit以 markdown 周报的形式输出到文件
    def write_2_md(self):
        file_name = self.name + '-commit-list.md'
        f = open(file_name, "w")
        print("#", self.name, "的 commit 周报\n", file = f)
        print("##", self.name, "在本周共有", self.commits_tot, "次 commits \n", file = f)
        index = 1
        for commit in self.commits:
            print("%d. [%s](%s) - %s \n" % (index, commit['message'], commit['url'], commit['time']), file = f)
            index += 1
        print("---", file = f)