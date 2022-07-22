# from asyncio.windows_events import NULL


def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    max_count = 0;
    max_freq_num = None;
    for num in nums:
        if (nums.count(num) > max_count):
            max_count = nums.count(num);
            max_freq_num = num;
    return max_freq_num;

print (mode([2, 2, 3, 3, 2]))
        # 2

print (mode([1, 2, 1]))
        # 1


# Alternatively
# Make frequency counter of num:freq
    # counts = {}

    # for num in nums:
    #     counts[num] = counts.get(num, 0) + 1

    # # find the highest value (the most frequent number)

    # max_value = max(counts.values())

    # # now we need to see at which index the highest value is at

    # for (num, freq) in counts.items():
    #     if freq == max_value:
    #         return num



