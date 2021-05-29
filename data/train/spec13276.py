import numpy as np 

def function(x):

	b2 = 1
	u1 = x
	x = x
	paths = []
	try:
		if u1 > 9:
			b2 = u1+7
			x = 3+x
			b2 = 6*b2
			paths.append(1)
		else:
			b2 = b2-x
			u1 = 8/2
			paths.append(2)
		if u1 <= 7:
			x = x*2
			x = x/5
			paths.append(3)
		else:
			b2 = b2/1
			u1 = u1+b2
			b2 = 6/b2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		b2 = b2**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))