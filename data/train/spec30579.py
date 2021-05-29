import numpy as np 

def function(x):

	u7 = x
	k2 = x
	paths = []
	try:
		if u7 <= 2:
			k2 = k2*6
			x = x*4
			k2 = k2+5
			paths.append(1)
		else:
			u7 = u7+7
			u7 = u7/2
			x = 8*x
			paths.append(2)
		if u7 >= 5:
			k2 = k2/1
			u7 = u7*0
			x = x/3
			paths.append(3)
		else:
			x = x-0
			u7 = u7/x
			x = 6/8
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))