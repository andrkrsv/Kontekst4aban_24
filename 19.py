print(' '.join( ( lambda x: sorted( set( word for word in x if x.count(word) > 1 ) ) )( [word for word in input().split('end')[0].split()] ) ) )
