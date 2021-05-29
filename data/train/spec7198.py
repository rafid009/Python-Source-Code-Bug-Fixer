import numpy as np 

def function(x):

	t4 = 2
	k9 = x
	paths = []
	try:
		if x <= 5:
			t4 = 2+8
			t4 = t4+x
			k9 = k9*9
			paths.append(1)
		else:
			x = x+9
			t4 = t4+x
			paths.append(2)
		if x < 7:
			x = t4*t4
			paths.append(3)
		else:
			x = x*x
			t4 = t4/k9
			t4 = k9/t4
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		x = k9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))