import numpy as np 

def function(x):

	t2 = x
	k6 = x
	paths = []
	try:
		if t2 > 2:
			k6 = 5-7
			x = t2+1
			paths.append(1)
		else:
			x = 6/6
			t2 = 2+t2
			paths.append(2)
		if k6 <= 9:
			x = 4-k6
			k6 = 3*k6
			k6 = k6*x
			paths.append(3)
		else:
			k6 = k6/3
			k6 = t2/k6
			k6 = x/t2
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))