import numpy as np 

def function(x):

	e3 = 1
	i6 = x
	paths = []
	try:
		if i6 > 1:
			i6 = i6+7
			paths.append(1)
		else:
			e3 = e3+i6
			e3 = x/9
			paths.append(2)
		if i6 <= 7:
			i6 = 8-i6
			paths.append(3)
		else:
			i6 = i6+7
			e3 = e3*6
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		i6 = e3**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))