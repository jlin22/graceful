use application "polytope";

my @files = ("1-1-1", "2-1-1", "3-1-1", "4-1-1", "5-1-1", "6-1-1", "7-1-1",
	     "8-1-1", "9-1-1", "10-1-1", "11-1-1");

sub construct_polytope {
    my $fn = $_[0];
    open(INPUT, "< ends/".$fn);
    my $A = new Matrix<Rational>(<INPUT>);
    close(INPUT);
    my $p = new Polytope(POINTS=>$A);
    my $n_ends = $A->rows;
    return($p, $n_ends);
}

sub gcd {
    my ($u, $v) = @_;
    while ($v) {
	($u , $v) = ($v, $u  % $v);
    }
    return $u;
}

sub gather_data {
    my @files = @_;
    foreach my $fn (@files) {
	my @a = construct_polytope($fn);
	my $p = $a[0];
	my $n_ends = $a[1];
	my $common_factor = gcd($n_ends, $p->N_LATTICE_POINTS);
	my @data = ("n_ends,".$n_ends, "n_lattice_points,".$p->N_LATTICE_POINTS, "n_facets,".$p->N_FACETS,
		    "n_edges,".$p->N_EDGES, "volume,".$p->VOLUME); 
	open(my $fh, '>', "data/".$fn."data");
	foreach my $entry (@data) {
	    print $fh $entry, "\n";
	}
	close $fh;
    }
}

gather_data(@files);
