# handy-py

A small repository in which I have documented the most handy Python snippets for solving programming puzzles.


> Borrowed from somewhere on the internet
```
If input array is sorted then
    - Binary search
    - Two pointers

If asked for all permutations/subsets then
    - Backtracking

If given a tree then
    - DFS
    - BFS

If given a graph then
    - DFS
    - BFS

If given a linked list then
    - Two pointers

If recursion is banned then
    - Stack

If must solve in-place then
    - Swap corresponding values
    - Store one or more different values in the same pointer

If asked for maximum/minimum subarray/subset/options then
    - Dynamic programming

If asked for top/least K items then
    - Heap
    - QuickSelect

If asked for common strings then
    - Map
    - Trie

Else
    - Map/Set for O(1) time & O(n) space
    - Sort input for O(nlogn) time and O(1) space
```

---

**Note on building the html docs:**

If in the root directory of the repo, run: `jb build .`
If in the parent directory of the repo, run: `jupyter-book build {repo_name}`

**Publishing to GitHub Pages:**

1. Install the `ghp-import` package: `pip install ghp-import`
2. run: `ghp-import -n -p -f _build/html` in the root directory of the repository

<!-- Useful links:
- [YouTube Tut](https://youtu.be/lZ2FHTkyaMU)
 -->
