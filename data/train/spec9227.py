import numpy as np 

def function(x):

	u7 = x
	i5 = x
	paths = []
	try:
		if i5 >= 4:
			i5 = x+3
			x = x-i5
			x = x/3
			paths.append(1)
		else:
			x = u7/9
			paths.append(2)
		if u7 <= 3:
			i5 = x-1
			u7 = 4+u7
			paths.append(3)
		else:
			i5 = 6-u7
			x = x*u7
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))