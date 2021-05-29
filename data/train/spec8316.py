import numpy as np 

def function(x):

	t8 = x
	k6 = 9
	paths = []
	try:
		if x <= 7:
			t8 = 4+t8
			paths.append(1)
		else:
			k6 = 7-k6
			x = x/9
			t8 = t8*2
			paths.append(2)
		if k6 < 9:
			x = x-t8
			paths.append(3)
		else:
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		t8 = t8**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))