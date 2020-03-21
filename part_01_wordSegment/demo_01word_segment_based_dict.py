# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2020/3/1 0001 10:36
import copy


def maximum_forward_matching_method(word_dict, waited_word_string):
    # 1 统计字典最常词语的长度
    # 数组中每个元素都是一个字符串
    max_length = max([len(word) for word in word_dict])

    # 2 列表接受分词
    result_word_list = []

    # 3 按正向(从左到右)的方向，首先以最大长度进行匹配
    word_index = 0
    new_string = copy.deepcopy(waited_word_string)

    while len(new_string) != 0:
        length = word_index + max_length
        # print(length)
        if waited_word_string[word_index:length] in word_dict:
            new_string = waited_word_string.replace(waited_word_string[word_index:length], "")

            # print(new_string)
            result_word_list.append(waited_word_string[word_index:length])
            # print(result_word_list)
            waited_word_string = copy.deepcopy(new_string)
            # print(waited_word_string)
            # 重置最大值
            max_length = max([len(word) for word in word_dict])
        else:
            max_length -= 1

    return result_word_list


def maximum_reverse_matching_method(word_dict, waited_word_string):
    # 1 统计字典最常词语的长度
    # 词典中每个元素都是一个字符串
    max_length = max([len(word) for word in word_dict])
    # 2 初始化列表接受分词
    result_word_list = []

    # 3 从逆向进行统计
    new_string = copy.deepcopy(waited_word_string)
    word_index = len(new_string)

    while len(new_string) != 0:
        # print(len(new_string))

        length = word_index - max_length
        # print(length)

        if length < 0:
            length = 0
        if waited_word_string[length:word_index] in word_dict:
            new_string = waited_word_string.replace(waited_word_string[length:word_index], "")
            # print(new_string)

            result_word_list.append(waited_word_string[length:word_index])
            # print(result_word_list)

            waited_word_string = copy.deepcopy(new_string)
            # print(waited_word_string)

            # 重置最大值
            max_length = max([len(word) for word in word_dict])

            # 剩余词的长度在变化
            word_index = len(new_string)
        else:
            max_length -= 1

    result_word_list.reverse()
    return result_word_list


def calculate_list_single_char_length(object_list):
    char_count = 0
    for string in object_list:
        if len(string) == 1:
            char_count += 1

    return char_count


def bidirectional_maximum_matching_algorithm(word_dict, waited_word_string):
    # 1 正向最大匹配算法
    maximum_forward_matching_result = maximum_forward_matching_method(word_dict, waited_word_string)
    print(maximum_forward_matching_result)
    # 2 逆向最大匹配算法
    maximum_reverse_matching_result = maximum_reverse_matching_method(word_dict, waited_word_string)
    print(maximum_reverse_matching_result)
    # 3 比较二者的分词数，分词数目不一样，取分词数量少的那一个。
    if len(maximum_forward_matching_result) < len(maximum_reverse_matching_result):
        return maximum_forward_matching_result
    # 选分词数目少的那个
    elif len(maximum_reverse_matching_result) < len(maximum_forward_matching_result):
        return maximum_reverse_matching_result
    # 数目相等时，比较结果，结果相同时都可以
    elif maximum_forward_matching_result == maximum_reverse_matching_result:
        return maximum_forward_matching_result
    # 结果不同时，选包含单字少的
    elif calculate_list_single_char_length(maximum_forward_matching_result) < calculate_list_single_char_length(
            maximum_reverse_matching_result):
        return maximum_forward_matching_result
    # 分词数相同，单字也相同，不在考虑。思路是包含2个字的最少的，递归。
    else:
        return maximum_reverse_matching_result


def main():

    word_dict = ["研究", "研究生", "生命", "命", "的", "起源"]
    waited_word_string = "研究生命的起源"

    result_forward = maximum_forward_matching_method(word_dict, waited_word_string)
    print("maximum_forward_matching_method：", result_forward)

    result_reverse = maximum_reverse_matching_method(word_dict, waited_word_string)
    print("maximum_reverse_matching_method：", result_reverse)

    bidirectional_result = bidirectional_maximum_matching_algorithm(word_dict, waited_word_string)
    print("bidirectional_maximum_matching_algorithm：", bidirectional_result)


if __name__ == '__main__':
    main()
