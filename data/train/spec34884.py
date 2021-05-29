import numpy as np 

def function(x):

	v2 = x
	t7 = 3
	paths = []
	try:
		if x <= 5:
			x = t7*7
			t7 = 4*4
			paths.append(1)
		else:
			x = v2*x
			v2 = v2/t7
			paths.append(2)
		if t7 <= 3:
			x = x+2
			t7 = v2+t7
			v2 = 8/v2
			paths.append(3)
		else:
			v2 = 2+v2
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		t7 = v2**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))