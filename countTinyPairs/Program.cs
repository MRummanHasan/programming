using System;

namespace countTinyPairs
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
             * Author: MRummanHasan
             * Date: 06-05-2019
             * Problem: Find tinypairs in 2 arrays; iterating left-rigth in array A & right-left in array B and concatinating respective values.
             * Return: No of int that are stricktly lesser than 'k'.
             *
             */

            int[] A = new int[] { 16, 1, 4, 2, 14 };
            int[] B = new int[] { 7, 11, 2, 0, 15 };
            int K = 743;

            int countTinyPairs(int[] a, int[] b, int k)
            {
                int count = 0;
                int j = b.Length - 1;
                for (int i = 0; i < a.Length; i++)
                {
                    int tempA = int.Parse(a[i].ToString() + b[j].ToString());
                    tempA = Convert.ToInt32(tempA);

                    if (tempA < k)
                        count++;

                    j--;
                }
                Console.ReadKey();
                return count;
            }
            countTinyPairs(A, B, K);
        }
    }
}
