import numpy as np 

def function(x):

	f9 = 3
	u7 = x
	paths = []
	try:
		if f9 <= 0:
			f9 = f9+1
			x = x-f9
			paths.append(1)
		else:
			x = x*5
			f9 = x+u7
			paths.append(2)
		if f9 <= 8:
			f9 = 4+f9
			paths.append(3)
		else:
			u7 = u7-6
			x = u7-1
			x = x/5
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		u7 = f9**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))