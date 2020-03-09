
def mySqrt(x: int) -> int:

        left = 0
        right = x

        while left <= right:

            mid = (right+left)//2

            if mid**2 == x:

                return mid

            elif mid**2 < x:

                left = mid + 1
                ans = mid

            else:

                right = mid - 1

        return ans

if __name__ == '__main__':

    print(mySqrt(8))
