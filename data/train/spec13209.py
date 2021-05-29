import numpy as np 

def function(x):

	u5 = 6
	j6 = x
	paths = []
	try:
		if u5 < 0:
			x = x-5
			paths.append(1)
		else:
			u5 = u5*0
			u5 = x+u5
			x = 4-x
			paths.append(2)
		if u5 <= 5:
			u5 = u5*9
			u5 = j6-u5
			x = x*j6
			paths.append(3)
		else:
			u5 = x+8
			j6 = j6+j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))