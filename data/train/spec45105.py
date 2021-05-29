import numpy as np 

def function(x):

	k1 = x
	u7 = x
	paths = []
	try:
		if x < 0:
			k1 = 9+k1
			paths.append(1)
		else:
			x = 7+0
			x = x*0
			k1 = x-2
			paths.append(2)
		if x <= 7:
			u7 = 2*8
			x = k1+1
			u7 = u7+7
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		k1 = k1**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))