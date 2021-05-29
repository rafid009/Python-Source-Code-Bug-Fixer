import numpy as np 

def function(x):

	v5 = x
	i6 = 2
	paths = []
	try:
		if x >= 9:
			x = x/5
			x = i6+i6
			paths.append(1)
		else:
			x = x/i6
			x = 6-x
			i6 = x+9
			paths.append(2)
		if x > 5:
			x = x-7
			i6 = 2-i6
			i6 = 8/i6
			paths.append(3)
		else:
			v5 = 9*v5
			i6 = 0-i6
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		i6 = v5**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))