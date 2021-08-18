from IsPalindromicPrime.PalindromicPrime import isPalindromicPrime
from IsPalindromicPrime.IsPalindromicPrime import IsPalindromicPrime
import os,sys
sys.path.append(os.getcwd())
from PalindromicPrime import isPalindromicPrime
import pytest


@pytest.mark.parametrize('m, result',[
	(2, True), (10, False),
	(104, False), (235, False),
	(131, True), (900, False),
	(101, True), (383, True),
	(373, True), (121, False)
])
def test(m, result):
    assert isPalindromicPrime(m) == result