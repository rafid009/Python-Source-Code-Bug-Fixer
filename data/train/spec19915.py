import numpy as np 

def function(x):

	k6 = 7
	v8 = 0
	paths = []
	try:
		if k6 <= 8:
			k6 = 4+k6
			x = x-2
			v8 = v8/3
			paths.append(1)
		else:
			x = 7+x
			x = x-x
			x = x*1
			paths.append(2)
		if v8 <= 9:
			k6 = 7*k6
			k6 = 5-k6
			paths.append(3)
		else:
			k6 = k6*k6
			k6 = v8+2
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		v8 = k6**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))