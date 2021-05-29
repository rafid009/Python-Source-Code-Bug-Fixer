import numpy as np 

def function(x):

	t1 = 8
	k1 = x
	x = x
	paths = []
	try:
		if k1 >= 8:
			k1 = k1+t1
			paths.append(1)
		else:
			t1 = 0*0
			x = x+0
			k1 = 4*7
			paths.append(2)
		if t1 <= 3:
			k1 = k1*7
			x = t1/6
			paths.append(3)
		else:
			t1 = 3-t1
			x = x-t1
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		k1 = t1**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))