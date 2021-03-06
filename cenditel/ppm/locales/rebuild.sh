i18ndude rebuild-pot --pot ./cenditel.ppm.pot --create cenditel.ppm ../ || exit 1
i18ndude sync --pot ./cenditel.ppm.pot ./*/LC_MESSAGES/cenditel.ppm.po

i18ndude rebuild-pot --pot ../i18n/ppm-plone.pot --merge ../i18n/manual.pot --create plone ../profiles || exit 1
i18ndude sync --pot ../i18n/ppm-plone.pot ../i18n/ppm-plone-*.po

ERRORS=`find ../ -name "*pt" | xargs i18ndude find-untranslated | grep -e '^-ERROR' | wc -l`
WARNINGS=`find ../ -name "*pt" | xargs i18ndude find-untranslated | grep -e '^-WARN' | wc -l`
FATAL=`find ../ -name "*pt"  | xargs i18ndude find-untranslated | grep -e '^-FATAL' | wc -l`

echo
echo "There are $ERRORS errors \(almost definitely missing i18n markup\)"
echo "There are $WARNINGS warnings \(possibly missing i18n markup\)"
echo "There are $FATAL fatal errors \(template could not be parsed, eg. if it\'s not html\)"
echo "For more details, run \'find . -name \"\*pt\" \| xargs i18ndude find-untranslated\' or" 
echo "Look the rebuild i18n log generate for this script called \'rebuild_i18n.log\' on locales dir" 

rm ./rebuild_i18n.log
touch ./rebuild_i18n.log

find ../ -name "*pt" | xargs i18ndude find-untranslated > ./rebuild_i18n.log
