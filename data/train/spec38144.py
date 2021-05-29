import numpy as np 

def function(x):

	t3 = x
	i6 = x
	paths = []
	try:
		if t3 < 9:
			i6 = 6/5
			i6 = 1-i6
			x = 3-4
			paths.append(1)
		else:
			t3 = 9*i6
			i6 = 4*5
			t3 = i6+t3
			paths.append(2)
		if t3 > 0:
			t3 = t3/x
			t3 = i6*1
			i6 = i6*8
			paths.append(3)
		else:
			x = x*8
			i6 = i6+i6
			t3 = t3-5
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))