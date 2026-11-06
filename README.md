# dsh-mp-a
dsh-superagent multi-project TEST repo A (safe to delete)

## 简单排序算法

使用 Python 3，无需安装第三方依赖。`sorting.py` 中的 `insertion_sort`
通过插入排序返回升序排列的新列表，不修改原列表。元素之间须可比较大小。

```python
from sorting import insertion_sort

numbers = [5, 2, 4, 2, -1]
print(insertion_sort(numbers))  # [-1, 2, 2, 4, 5]
print(numbers)                  # [5, 2, 4, 2, -1]
```

插入排序逐个将元素插入前面已排好序的部分，适合学习和处理少量数据。
它是稳定排序，最坏时间复杂度为 O(n²)，已排序输入为 O(n)，
为保留原列表使用 O(n) 额外空间。

运行测试：

```sh
python3 -m unittest discover -v
```
