pdb2pqr --ff=AMBER --with-ph=7.0 --titration-state-method propka --drop-water idoA_fixed.pdb ido_ph7_amber.pqr
pdb2pqr --ff=AMBER --with-ph=7.0 --titration-state-method propka --drop-water tdoA_fixed.pdb tdo_ph7_amber.pqr
cat ido_ph7_amber.pqr heme.pqr > ido_ph7_amber.pqr
cat tdo_ph7_amber.pqr heme.pqr > tdo_ph7_amber.pqr
./apbs apbs_ido.in
./apbs apbs_tdo.in
