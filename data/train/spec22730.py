import numpy as np 

def function(x):

	t1 = 9
	v6 = x
	paths = []
	try:
		if t1 > 8:
			x = x-v6
			v6 = v6/6
			t1 = t1+t1
			paths.append(1)
		else:
			v6 = 3-2
			paths.append(2)
		if t1 >= 4:
			x = t1-5
			v6 = v6*2
			t1 = t1*1
			paths.append(3)
		else:
			v6 = v6+9
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		x = v6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))