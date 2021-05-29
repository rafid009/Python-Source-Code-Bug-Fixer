import numpy as np 

def function(x):

	v7 = 5
	t6 = x
	paths = []
	try:
		if x <= 3:
			v7 = 3+x
			paths.append(1)
		else:
			t6 = t6+1
			paths.append(2)
		if v7 < 8:
			v7 = 3/t6
			paths.append(3)
		else:
			t6 = 7*t6
			t6 = 6+t6
			v7 = x/v7
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		v7 = v7**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))