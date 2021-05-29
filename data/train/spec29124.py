import numpy as np 

def function(x):

	a8 = x
	i5 = 9
	paths = []
	try:
		if i5 <= 7:
			i5 = i5/a8
			x = 8-x
			paths.append(1)
		else:
			i5 = i5*0
			a8 = a8/2
			paths.append(2)
		if i5 < 6:
			a8 = a8-5
			i5 = i5*i5
			paths.append(3)
		else:
			a8 = 7*9
			a8 = 3+a8
			x = x*9
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		i5 = a8**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))