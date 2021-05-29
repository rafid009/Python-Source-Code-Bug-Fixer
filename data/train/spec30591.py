import numpy as np 

def function(x):

	t8 = x
	k5 = x
	paths = []
	try:
		if t8 <= 9:
			k5 = k5+1
			paths.append(1)
		else:
			t8 = t8*4
			t8 = k5/6
			k5 = k5*1
			paths.append(2)
		if k5 < 3:
			x = x-3
			t8 = x+2
			x = 4-x
			paths.append(3)
		else:
			x = 2+1
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		k5 = t8**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))