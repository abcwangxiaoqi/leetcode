#思路 转成数组 相加后再转成对象


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):

    # 我的方法
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ResNums=[]

        tmpAd=0

        while (l1==None and l2==None)==False:
            n1=0
            if l1!=None:
                n1=l1.val
                l1=l1.next
            n2=0
            if l2 != None:
                n2 = l2.val
                l2=l2.next
            cou=n1+n2+tmpAd
            cur=0
            if cou>=10:
                cur=cou-10
                tmpAd=1
            else:
                cur=cou
                tmpAd=0

            ResNums.append(cur)

        if tmpAd>0:
            ResNums.append(tmpAd)

        return self.OutListNode(ResNums)
    def OutListNode(self,l,cur=0):
        '''
        :param l: []
        :return:ListNode
        '''

        if l==None:
            return None

        if cur<len(l):
            list = ListNode(l[cur])
            cur+=1
            list.next=self.OutListNode(l,cur)
            return list
        else:
            return None

    # 其他算法思路
    def addTwoNumbers2(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next






L1=[2,3,4,5,6]
L2=[5,6,7,8,3]
so=Solution()
l1=so.OutListNode(L1)
l2=so.OutListNode(L2)

res=so.addTwoNumbers2(l1,l2)

while res!=None:
    print(res.val)
    res=res.next