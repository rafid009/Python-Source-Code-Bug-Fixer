import numpy as np 

def function(x):

	t7 = 1
	i7 = 4
	x = 6
	paths = []
	try:
		if x >= 2:
			i7 = t7+i7
			t7 = 2-t7
			paths.append(1)
		else:
			x = i7-x
			x = 3+x
			i7 = 5/i7
			paths.append(2)
		if i7 > 1:
			i7 = 0-i7
			x = 4*x
			t7 = 3-t7
			paths.append(3)
		else:
			t7 = t7*i7
			t7 = 4/t7
			i7 = 7+t7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		t7 = i7**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))