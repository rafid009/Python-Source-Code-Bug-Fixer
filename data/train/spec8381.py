import numpy as np 

def function(x):

	i5 = x
	b9 = x
	paths = []
	try:
		if x > 4:
			i5 = i5-x
			b9 = 3-4
			i5 = 6-1
			paths.append(1)
		else:
			x = 2+i5
			b9 = b9*i5
			paths.append(2)
		if i5 <= 1:
			i5 = i5-5
			paths.append(3)
		else:
			x = b9/9
			i5 = i5*9
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