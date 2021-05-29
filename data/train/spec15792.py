import numpy as np 

def function(x):

	v2 = x
	t8 = 5
	paths = []
	try:
		if t8 < 0:
			v2 = 6*2
			t8 = t8/1
			paths.append(1)
		else:
			v2 = 9+4
			v2 = v2+x
			v2 = v2*v2
			paths.append(2)
		if t8 < 4:
			t8 = 0/x
			paths.append(3)
		else:
			v2 = v2-2
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))