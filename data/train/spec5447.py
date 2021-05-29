import numpy as np 

def function(x):

	t6 = x
	i0 = 1
	x = x
	paths = []
	try:
		if t6 < 7:
			i0 = 7*i0
			x = x*7
			i0 = 9/4
			paths.append(1)
		else:
			i0 = x-0
			t6 = t6+t6
			t6 = i0-t6
			paths.append(2)
		if i0 <= 2:
			x = x/i0
			paths.append(3)
		else:
			i0 = i0*4
			i0 = i0-5
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		i0 = t6**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))