import numpy as np 

def function(x):

	t1 = x
	i6 = 3
	paths = []
	try:
		if i6 <= 0:
			x = x-x
			paths.append(1)
		else:
			x = x+i6
			t1 = 3*t1
			paths.append(2)
		if x > 2:
			t1 = i6-6
			paths.append(3)
		else:
			i6 = 5/i6
			x = x/7
			i6 = i6+x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))