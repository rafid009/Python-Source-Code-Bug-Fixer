import numpy as np 

def function(x):

	t7 = 8
	k9 = x
	paths = []
	try:
		if k9 >= 7:
			t7 = 4*t7
			x = x-k9
			paths.append(1)
		else:
			k9 = t7*0
			t7 = t7+x
			paths.append(2)
		if k9 <= 9:
			t7 = x*t7
			x = k9+t7
			x = 7*x
			paths.append(3)
		else:
			k9 = k9+0
			x = k9+x
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))