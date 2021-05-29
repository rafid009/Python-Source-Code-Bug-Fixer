import numpy as np 

def function(x):

	u5 = x
	u3 = x
	paths = []
	try:
		if x >= 0:
			u3 = 5/7
			u5 = 3+x
			x = x*0
			paths.append(1)
		else:
			u5 = u5+0
			x = 7/u3
			u3 = u3/u3
			paths.append(2)
		if u5 > 4:
			x = 4+u5
			u3 = 6-x
			u5 = u3*u5
			paths.append(3)
		else:
			u5 = u5-u5
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u3 = u3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))