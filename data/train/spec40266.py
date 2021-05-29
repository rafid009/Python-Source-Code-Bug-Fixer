import numpy as np 

def function(x):

	t6 = x
	i1 = 3
	paths = []
	try:
		if t6 < 4:
			t6 = t6-7
			paths.append(1)
		else:
			t6 = t6-t6
			x = i1-0
			paths.append(2)
		if i1 > 5:
			x = 7*x
			paths.append(3)
		else:
			t6 = t6/i1
			i1 = i1/i1
			i1 = 4/7
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		i1 = t6**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))