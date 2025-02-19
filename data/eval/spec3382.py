import numpy as np 

def function(x):

	v9 = x
	u5 = x
	paths = []
	try:
		if u5 <= 5:
			x = x+9
			u5 = 2/6
			u5 = u5*u5
			paths.append(1)
		else:
			x = x+x
			u5 = u5/6
			paths.append(2)
		if u5 >= 2:
			u5 = u5+1
			paths.append(3)
		else:
			v9 = v9*1
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		v9 = v9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))