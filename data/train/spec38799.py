import numpy as np 

def function(x):

	i3 = x
	t1 = x
	paths = []
	try:
		if x < 8:
			i3 = 3*x
			i3 = t1/i3
			i3 = i3*1
			paths.append(1)
		else:
			i3 = 6*4
			t1 = t1/t1
			x = x*3
			paths.append(2)
		if t1 > 8:
			x = 8+x
			paths.append(3)
		else:
			t1 = t1+7
			i3 = 9+t1
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		x = t1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))