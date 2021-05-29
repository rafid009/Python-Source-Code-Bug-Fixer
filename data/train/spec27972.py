import numpy as np 

def function(x):

	t5 = x
	i4 = 3
	paths = []
	try:
		if t5 < 7:
			i4 = t5-i4
			x = t5*x
			t5 = 3+i4
			paths.append(1)
		else:
			t5 = t5+0
			paths.append(2)
		if x < 6:
			i4 = t5-8
			paths.append(3)
		else:
			t5 = t5*2
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))