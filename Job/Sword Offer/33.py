# 二叉搜索树的后序遍历序列
from typing import List


class Solution:
    # 递归分治的思想
    # 每次先通过比较大小将序列的左右子树区间找出来
    # 通过判断左子树区间元素全部小于根，右子树区间元素全部大于根，来判断当前树是否为二叉搜索树
    # 不符合条件则直接返回false，符合条件则递归的判断左右子树是不是二叉搜索树
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(start: int, end: int) -> bool:
            # 如果树的结点数目小于等于1，则肯定是二叉搜索树
            if start >= end:
                return True
            root = postorder[end]
            # mid的初始化很重要，如果右子树为空，mid需要赋值为end
            mid = end
            # 通过寻找第一个大于root的元素，找到右子树左边界
            for i in range(start, end):
                if postorder[i] > root:
                    mid = i
                    break
            # 判断右子树中是否存在小于root的元素
            for j in range(mid, end):
                if postorder[j] < root:
                    return False
            # 左右子树均为二叉搜索树，则该树为二叉搜索树
            return recur(start, mid - 1) and recur(mid, end - 1)

        return recur(0, len(postorder) - 1)


if __name__ == '__main__':
    seq = [39, 80, 199, 215, 90, 397, 465, 385, 362, 513, 588, 741, 711, 1023, 706, 510, 1135, 1071, 1374, 1320, 1204,
           1495, 1657, 2038, 1775, 1526, 1400, 2109, 2148, 2140, 2338, 2300, 1042, 44, 2566, 2599, 2441, 2832, 3314,
           3189, 3089, 2969, 3395, 3485, 3456, 3403, 3700, 3646, 3812, 3840, 4191, 4372, 3917, 4939, 4754, 4575, 3740,
           5355, 5538, 5175, 5104, 3568, 3353, 3321, 2675, 5575, 5660, 5574, 2409, 6142, 6059, 6153, 6207, 5893, 6664,
           6612, 7176, 7154, 6669, 6466, 7705, 7853, 8317, 8416, 8334, 8310, 8273, 7825, 8719, 9037, 8670, 9050, 9672,
           10015, 9941, 9788, 10075, 10352, 10020, 9441, 10522, 10572, 10682, 10676, 10583, 10434, 10861, 10784, 8511,
           7492, 11116, 11045, 11557, 11909, 11957, 12076, 11945, 11941, 12305, 12199, 11782, 11425, 12337, 12809,
           12901, 12609, 13128, 13320, 13733, 13654, 13345, 12947, 12312, 14131, 13876, 14191, 14461, 14756, 14755,
           14520, 14816, 14850, 14870, 14763, 14897, 14163, 15037, 15221, 15625, 15504, 15776, 15839, 15975, 16527,
           16425, 15824, 15812, 16654, 15114, 16801, 17016, 16949, 16873, 16769, 17226, 17029, 16708, 17272, 17459,
           17523, 17260, 15000, 17712, 17898, 17856, 17944, 17943, 18145, 17921, 18341, 18264, 18663, 18480, 19191,
           19006, 19258, 19273, 19201, 19391, 19576, 19606, 19723, 19831, 19855, 19964, 19760, 19629, 19365, 18459,
           18261, 20337, 19995, 20388, 20384, 20659, 21073, 20923, 20567, 21123, 21360, 21547, 21378, 21354, 21584,
           21574, 21644, 21798, 21903, 21956, 22052, 22030, 22054, 22214, 22457, 22589, 22734, 22511, 22493, 22182,
           22018, 23056, 22896, 22751, 21816, 21641, 21241, 19979, 23308, 23600, 23494, 23429, 23723, 23698, 23259,
           17560, 23868, 23964, 23995, 24313, 24306, 24378, 24355, 23947, 23894, 24444, 24478, 24996, 24873, 25099,
           25111, 25263, 25467, 25405, 25338, 25185, 25059, 24442, 25881, 26457, 26100, 25997, 25722, 25621, 23745,
           26761, 26860, 26814, 26975, 26996, 26989, 26969, 26553, 13734, 27644, 27872, 27340, 27928, 27995, 28431,
           28161, 28061, 27914, 28816, 28783, 29216, 29348, 29630, 29520, 29375, 29732, 29164, 28553, 27221, 30054,
           30275, 30104, 30360, 30053, 30610, 30549, 30946, 30934, 30947, 30860, 31189, 31274, 31018, 31314, 31333,
           31366, 31335, 31479, 31752, 31884, 32021, 31980, 31766, 32153, 31408, 31286, 32690, 32865, 32949, 32703,
           33093, 33393, 33398, 33579, 33509, 33592, 33694, 33760, 33698, 34001, 33975, 33932, 33772, 33589, 33129,
           33066, 34294, 34423, 34341, 34161, 34534, 34606, 35088, 34836, 34474, 35094, 34440, 32313, 29961, 11013,
           5804, 35153, 35409, 35496, 35271, 35998, 36109, 36217, 36335, 36412, 36691, 36782, 36662, 36569, 36468,
           35562, 35237, 35178, 36898, 36862, 37118, 37142, 37358, 37194, 37096, 36922, 37745, 37893, 37808, 37898,
           37757, 37739, 37962, 38350, 38489, 38427, 38331, 37991, 38530, 38564, 38501, 38604, 37928, 38789, 39080,
           38930, 39554, 39522, 39746, 39664, 39349, 38685, 40233, 40185, 40629, 40697, 41403, 40699, 41484, 41748,
           41687, 41959, 41939, 42068, 41858, 41843, 41481, 42342, 42200, 42593, 42395, 42700, 42713, 42861, 42919,
           42751, 42653, 43190, 43024, 43308, 43647, 43676, 44032, 44204, 44080, 43677, 43463, 44433, 44593, 44602,
           44680, 44493, 44322, 45249, 45373, 45366, 44840, 44790, 44782, 43223, 42390, 45659, 45759, 45888, 45921,
           45890, 45795, 45940, 45707, 45973, 46014, 46013, 45948, 46263, 46612, 46800, 46535, 46305, 46256, 46905,
           47224, 47487, 47286, 47582, 46819, 45945, 47736, 47676, 47962, 48158, 48273, 47973, 48704, 48865, 48823,
           49112, 49427, 49475, 49416, 49145, 48883, 47858, 49532, 49605, 50062, 49715, 49477, 47625, 45645, 42156,
           50436, 50533, 50593, 50437, 50759, 50763, 50747, 51201, 51350, 51945, 51038, 50868, 50852, 52337, 52011,
           52482, 52343, 52657, 52741, 52553, 51994, 53023, 53138, 53062, 53236, 53253, 53318, 53497, 53745, 53678,
           53632, 53156, 54010, 54259, 54297, 54105, 54320, 54609, 54599, 54882, 54694, 54659, 54641, 54344, 54306,
           53808, 55355, 55464, 55240, 55177, 55608, 55649, 55797, 55832, 56031, 56052, 55888, 55563, 55540, 56550,
           56583, 56355, 55483, 55141, 53140, 56881, 56998, 57011, 57205, 56856, 57952, 57503, 58244, 58238, 58066,
           57412, 52801, 58410, 58431, 58511, 58470, 58623, 58674, 58772, 58826, 58720, 58875, 58922, 58856, 59011,
           58520, 58355, 59201, 59120, 59476, 59228, 60122, 59824, 59505, 60440, 60401, 60625, 60663, 60615, 60718,
           60525, 61139, 60886, 59215, 61264, 61213, 61469, 61656, 61639, 61728, 61676, 62098, 61842, 61572, 62164,
           61312, 62341, 62406, 62792, 62816, 62907, 62360, 62310, 63076, 63230, 63064, 63389, 63460, 63660, 63747,
           64097, 64324, 64339, 64431, 64156, 64518, 64946, 65055, 64597, 63896, 63251, 65257, 65168, 62187, 61160,
           58260, 50315, 65521, 65575, 65833, 65711, 65552, 66074, 66697, 66509, 66391, 66816, 66914, 66954, 66942,
           67236, 67045, 66993, 67338, 67330, 67351, 67427, 67573, 67481, 67753, 67586, 67369, 67253, 67879, 67775,
           68064, 67940, 67774, 67771, 66917, 68399, 68456, 68758, 69085, 69528, 69576, 69575, 69558, 69423, 69049,
           69668, 70049, 70095, 70000, 70182, 69867, 70501, 69658, 70786, 70808, 70893, 70890, 70549, 69581, 71028,
           70958, 71337, 71104, 71416, 71732, 71693, 71541, 71941, 71962, 71910, 71824, 72576, 72782, 72958, 72823,
           72465, 73888, 73630, 73479, 73206, 74030, 74147, 74058, 74054, 74159, 73159, 72454, 71402, 74479, 75135,
           75185, 75690, 75602, 75560, 75527, 75525, 75174, 76047, 76071, 75916, 76138, 75884, 75141, 74940, 74194,
           68103, 65981, 65259, 76276, 76426, 76293, 76561, 76627, 76479, 76639, 76775, 76803, 77108, 77694, 77292,
           77710, 76978, 76840, 77926, 78113, 77876, 76791, 78297, 78463, 78783, 79326, 79522, 79192, 78156, 76730,
           76252, 79652, 79871, 79903, 80086, 79940, 80349, 80259, 80247, 80566, 79724, 79640, 80807, 81032, 81077,
           81060, 80820, 81745, 81765, 81672, 81908, 81267, 82128, 82113, 82370, 82346, 82400, 82499, 82553, 82569,
           82751, 82658, 82403, 82373, 83499, 83467, 83438, 83330, 83515, 83676, 83644, 83239, 82804, 82229, 83941,
           83801, 84200, 84223, 84298, 84323, 84408, 84242, 84008, 84427, 84678, 84650, 84744, 85083, 85318, 85286,
           85427, 85366, 85099, 85964, 85615, 86000, 85989, 86363, 86734, 86941, 86911, 86835, 86762, 86994, 86721,
           85516, 84995, 84416, 87185, 87580, 87648, 87812, 87693, 87834, 87957, 87978, 87922, 87627, 88411, 88201,
           88051, 88464, 89058, 88977, 89303, 89428, 89344, 89258, 89806, 90040, 89128, 90154, 90254, 90358, 90287,
           90889, 90272, 91162, 90193, 90047, 91224, 91688, 91566, 91908, 91835, 91217, 92443, 92551, 92222, 92674,
           93496, 93511, 93509, 93560, 93539, 93828, 93721, 93100, 92594, 91941, 88450, 87049, 83689, 93932, 94108,
           94379, 94684, 94592, 94914, 94692, 95161, 95209, 95080, 95302, 95023, 95424, 95358, 95308, 94920, 95503,
           95567, 95560, 95428, 95852, 96296, 96476, 96480, 96100, 97306, 97240, 97227, 97053, 96857, 96687, 95841,
           94078, 98060, 98061, 97459, 97457, 98129, 98225, 98506, 98638, 98604, 98587, 98539, 98847, 98849, 98878,
           98656, 98930, 98179, 99019, 98119, 99063, 99211, 99104, 99055, 99020, 99562, 99684, 99974, 99815, 99717,
           99687, 99251, 93923, 80776, 39833, 35138]
    print(Solution().verifyPostorder(seq))
