import numpy as np 

def function(x):

	i7 = 5
	u7 = 7
	paths = []
	try:
		if i7 > 8:
			i7 = i7-8
			u7 = u7*2
			paths.append(1)
		else:
			x = 8*0
			x = u7/8
			paths.append(2)
		if i7 <= 7:
			u7 = u7/5
			u7 = u7-4
			paths.append(3)
		else:
			x = x*5
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		x = u7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))