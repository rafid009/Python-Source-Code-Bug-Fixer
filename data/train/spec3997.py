import numpy as np 

def function(x):

	u7 = x
	w5 = 6
	paths = []
	try:
		if x < 6:
			w5 = x/1
			w5 = 8*9
			u7 = 6/u7
			paths.append(1)
		else:
			w5 = x*0
			paths.append(2)
		if u7 <= 1:
			x = 6/7
			paths.append(3)
		else:
			u7 = u7+x
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		u7 = u7**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))