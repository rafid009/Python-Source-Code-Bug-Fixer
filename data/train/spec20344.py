import numpy as np 

def function(x):

	k6 = x
	u1 = 5
	paths = []
	try:
		if u1 >= 9:
			k6 = 7+k6
			x = u1/u1
			paths.append(1)
		else:
			k6 = x+3
			x = 8-6
			u1 = u1-9
			paths.append(2)
		if u1 <= 4:
			u1 = u1*5
			paths.append(3)
		else:
			u1 = 4+x
			u1 = u1*5
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		k6 = k6**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))