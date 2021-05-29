import numpy as np 

def function(x):

	t2 = x
	b3 = 6
	x = x
	paths = []
	try:
		if t2 <= 2:
			b3 = 6+7
			t2 = b3/t2
			paths.append(1)
		else:
			b3 = 4-b3
			paths.append(2)
		if b3 < 6:
			x = x+4
			t2 = 7/1
			paths.append(3)
		else:
			t2 = x+t2
			b3 = 9+b3
			t2 = t2+2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		b3 = t2**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))